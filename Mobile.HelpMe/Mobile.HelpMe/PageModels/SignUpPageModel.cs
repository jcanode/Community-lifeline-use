using System;
using System.Threading.Tasks;
using System.Windows.Input;
using FreshMvvm;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.Models;
using Xamarin.Forms;

namespace Mobile.HelpMe.PageModels
{
    public class SignUpPageModel : BaseViewModel
    {


        #region Properties

        public string PasswordMatchError { get; set; } = AppConstants.PasswordsDontMatch;
        public string PasswordLengthError { get; set; } = AppConstants.PasswordLength;
        public string EmptyFieldsError { get; set; } = AppConstants.EmptyFieldError;

        private string _username;
        public string Username
        {
            get => _username;
            set => SetValue(ref _username, value);
        }

        private string _password;
        public string Password
        {
            get => _password;
            set => SetValue(ref _password, value);
        }

        private string _email;
        public string Email
        {
            get => _email;
            set => SetValue(ref _email, value);
        }

        private string _confirmPass;
        public string ConfirmPass
        {
            get => _confirmPass;
            set => SetValue(ref _confirmPass, value);
        }

        private string _phoneNumber;
        public string PhoneNumber
        {
            get => _phoneNumber;
            set => SetValue(ref _phoneNumber, value);
        }

        private bool _passwordsNotMatch = false;
        public bool PasswordsNotMatch
        {
            get => _passwordsNotMatch;
            set => SetValue(ref _passwordsNotMatch, value);
        }

        private bool _passwordNotCorrectLength = false;
        public bool PasswordNotCorrectLength
        {
            get => _passwordNotCorrectLength;
            set => SetValue(ref _passwordNotCorrectLength, value);
        }

        private bool _emptyField = false;
        public bool EmptyFields
        {
            get => _emptyField;
            set => SetValue(ref _emptyField, value);
        }
        #endregion

        #region Commands
        public ICommand CreateAccountClicked { get; }
        #endregion

        #region IoC Members
        private IUserService _userService;
        #endregion

        public SignUpPageModel(IUserService userService)
        {
            _userService = userService;

            CreateAccountClicked = new Command(async () => await OnCreatedAccountClicked());
        }

        private async Task OnCreatedAccountClicked()
        {
            if (!string.IsNullOrEmpty(_password) && !string.IsNullOrEmpty(_email) && !string.IsNullOrEmpty(_username) && !string.IsNullOrEmpty(_confirmPass))
            {
                if (!_password.Trim().Equals(_confirmPass.Trim()))
                    PasswordsNotMatch = true;
                if (_password.Length < AppConstants.PasswordLengthConstant)
                    PasswordNotCorrectLength = true;
                else
                {
                    PasswordsNotMatch = false;
                    PasswordNotCorrectLength = false;
                    EmptyFields = false;
                    User user = new User
                    {
                        Email = _email,
                        UserName = _username,
                        Password = _password,
                        PhoneNumber = _phoneNumber,
                        HelpRating = 0
                    };

                    await _userService.CreateUser(user);


                    var tabbedNav = new FreshTabbedNavigationContainer("secondNavPage");
                    tabbedNav.AddTab<MainPageModel>("Home", null);
                    tabbedNav.AddTab<HelpMePageModel>("Help Me", null);
                    tabbedNav.AddTab<HelpYouPageModel>("Help You", null);

                    await CoreMethods.PushNewNavigationServiceModal(tabbedNav);
                }
            }
            else
            {
                EmptyFields = true;
            }
        }
    }
}

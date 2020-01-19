using System;
using System.Threading.Tasks;
using System.Windows.Input;
using FreshMvvm;
using Mobile.HelpMe.Interfaces.Services;
using Xamarin.Forms;

namespace Mobile.HelpMe.PageModels
{
    public class SignInPageModel : BaseViewModel
    {
        #region IoC Members
        IUserService _userService;
        #endregion


        #region Properties
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

        #endregion

        #region Commands
        public ICommand SignInClicked { get; private set; }
        public ICommand SignUpClicked { get; private set;  }
        #endregion

        public SignInPageModel(IUserService userService)
        {
            _userService = userService;

            SignInClicked = new Command(async () => await OnSignInClicked());
            SignUpClicked = new Command(async () => await OnSignUpClicked());
        }

        private async Task OnSignInClicked()
        {
            await _userService.SignIn(Username, Password);
            var tabbedNav = new FreshTabbedNavigationContainer("secondNavPage");
            tabbedNav.AddTab<MainPageModel>("Home", null);
            tabbedNav.AddTab<HelpMePageModel>("Help Me", null);
            tabbedNav.AddTab<HelpYouPageModel>("Help You", null);

            await CoreMethods.PushNewNavigationServiceModal(tabbedNav);
        }

        private async Task OnSignUpClicked()
        {
            await CoreMethods.PushPageModel<SignUpPageModel>();
        }
    }
}

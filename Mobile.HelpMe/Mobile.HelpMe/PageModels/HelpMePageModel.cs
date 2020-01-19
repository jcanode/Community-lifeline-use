using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Windows.Input;
using FreshMvvm;
using Mobile.HelpMe.Models;
using Xamarin.Essentials;
using Xamarin.Forms;

namespace Mobile.HelpMe.PageModels
{
    public class HelpMePageModel : BaseViewModel
    {
        #region Picker Lists
        public IList<string> Categories { get; } = AppConstants.Categories;
        public IList<string> CarProblems { get; } = AppConstants.CarProblems;
        public IList<string> NaturalDisasterProblems { get; } = AppConstants.NaturalDisasterProblems;
        #endregion

        #region Commands
        public ICommand SubmitButtonClicked { get; }
        #endregion

        #region Properties
        private string _selectedCategory;
        public string SelectedCategory
        {
            get => _selectedCategory;
            set
            {
                SetValue(ref _selectedCategory, value);
                DeterminePickerToShow(_selectedCategory);
            }
        }

        private string _selectedNdProblem;
        public string SelectedNdProblem
        {
            get => _selectedNdProblem;
            set
            {
                ShouldShowDescription(value);
                SetValue(ref _selectedNdProblem, value);
                
            }
        }

        private string _selectedCarProblem;
        public string SelectedCarProblem
        {
            get => _selectedCarProblem;
            set
            {
                ShouldShowDescription(value);
                SetValue(ref _selectedCarProblem, value);

            }
        }

        private bool _showDescription = false;
        public bool ShowDescription
        {
            get => _showDescription;
            set
            {
                SetValue(ref _showDescription, value);
            }
        }

        private bool _showCarProblemList = false;
        public bool ShowCarProblemList
        {
            get => _showCarProblemList;
            set => SetValue(ref _showCarProblemList, value);
        }

        private bool _showNaturalDisasterProblemList = false;
        public bool ShowNaturalDisasterList
        {
            get => _showNaturalDisasterProblemList;
            set => SetValue(ref _showNaturalDisasterProblemList, value);
        }

        private string _problemDesc;
        public string ProblemDesc
        {
            get => _problemDesc;
            set
            {
                SetValue(ref _problemDesc, value);
            }
        }
        #endregion

        public HelpMePageModel()
        {
            SubmitButtonClicked = new Command(async () => await OnSubmitClicked());
        }

        

        private void ShouldShowDescription(string selectedProblem)
        {
            if (selectedProblem.Equals("Other"))
                ShowDescription = true;
            else
                ShowDescription = false;
        }

        private void DeterminePickerToShow(string selectedCategory)
        {
            if (selectedCategory.Equals("Car"))
            {
                ShowNaturalDisasterList = false;
                ShowCarProblemList = true;
            }
            else if (selectedCategory.Equals("Natural Disaster"))
            {
                ShowCarProblemList = false;
                ShowNaturalDisasterList = true;
            }

        }

        private async Task OnSubmitClicked()
        {
            var location = await Geolocation.GetLastKnownLocationAsync();
            var request = new HelpRequest
            {
                Problem = SelectedCategory == "Car" ? SelectedCarProblem : SelectedNdProblem,
                Description = ProblemDesc,
                Latitude = location.Latitude,
                Longitude = location.Longitude,
                UserEmail = "jcanode@nomail.com",
                Username = "jcanode"
            };

            await CoreMethods.DisplayAlert(AppConstants.RequestSentTitle, AppConstants.RequestSentMessage, AppConstants.OkayText, AppConstants.OkayText);
            await CoreMethods.SwitchSelectedTab<MainPageModel>();
        }

    }
}

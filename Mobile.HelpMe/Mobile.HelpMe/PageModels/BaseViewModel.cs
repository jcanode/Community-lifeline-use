using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;
using FreshMvvm;

namespace Mobile.HelpMe.PageModels
{
    public class BaseViewModel : FreshBasePageModel, INotifyPropertyChanged
    {
        public new event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        protected void SetValue<T>(ref T backingField, T value, [CallerMemberName] string propertyName = null)
        {
            if (EqualityComparer<T>.Default.Equals(backingField, value)) return;
            backingField = value;
            OnPropertyChanged(propertyName);
        }

        public async Task NavigateToMainTabbedPage()
        {
            var tabbedNav = new FreshTabbedNavigationContainer();
            tabbedNav.AddTab<MainPageModel>("Home", null);
            tabbedNav.AddTab<HelpMePageModel>("Help Me", null);
            tabbedNav.AddTab<HelpYouPageModel>("Help You", null);
            tabbedNav.AddTab<SignUpPageModel>("Sign Up", null);
            tabbedNav.AddTab<SignInPageModel>("Sign In", null);

            await CoreMethods.PushNewNavigationServiceModal(tabbedNav);
        }
    }
}

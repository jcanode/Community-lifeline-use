using System;
using FreshMvvm;
using Mobile.HelpMe.PageModels;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Mobile.HelpMe
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            var mainpage = new FreshTabbedNavigationContainer();

            mainpage.AddTab<MainPageModel>("Home", null);
            mainpage.AddTab<MainPageModel>("Help Me", null);
            mainpage.AddTab<MainPageModel>("Help You", null);


            MainPage = mainpage;
        }

        protected override void OnStart()
        {
            // Handle when your app starts
        }

        protected override void OnSleep()
        {
            // Handle when your app sleeps
        }

        protected override void OnResume()
        {
            // Handle when your app resumes
        }
    }
}

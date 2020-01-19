using System;
using FreshMvvm;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.PageModels;
using Mobile.HelpMe.Services;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Mobile.HelpMe
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            FreshIoCManager.RegisterServices();

            var page = FreshPageModelResolver.ResolvePageModel<SignInPageModel>();
            var basicNav = new FreshNavigationContainer(page);
            MainPage = basicNav;

            
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

using System;
using FreshMvvm;
using Mobile.HelpMe.Interfaces.Repository;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.Repositories;
using Mobile.HelpMe.Services;

namespace Mobile.HelpMe
{
    public static class FreshIoCManager
    {
        public static void RegisterServices()
        {
            // Services
            FreshIOC.Container.Register<IUserService, UserService>().AsSingleton();
            FreshIOC.Container.Register<IGeolocationCalculations, GeolocationCalculations>().AsSingleton();
            FreshIOC.Container.Register<IHelpRequestService, HelpRequestService>().AsSingleton();

            // Repositories
            FreshIOC.Container.Register<IUserRepository, UserRepository>().AsSingleton();
            FreshIOC.Container.Register<IHelpRequestRepository, HelpRequestRepository>().AsSingleton();
        }
    }
}

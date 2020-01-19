using System;
using System.Collections.ObjectModel;
using FreshMvvm;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.PageModels
{
    public class HelpYouPageModel : FreshBasePageModel
    {
        private double userLat = 33.447130;
        private double userLong = -112.075545;

        #region IoC Members
        private IGeolocationCalculations _geoCalculations;
        #endregion

        #region Public Properties
        public ObservableCollection<HelpRequest> HelpRequests { get; private set; }
        #endregion

        public HelpYouPageModel(IGeolocationCalculations geoCalculations)
        {
            _geoCalculations = geoCalculations;
        }


        public override void Init(object initData)
        {
            base.Init(initData);
            HelpRequests = new ObservableCollection<HelpRequest>
            {
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = "FlatTire",
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
            };

            foreach(var item in HelpRequests)
            {
                item.Distance = _geoCalculations.CalculateDistance(userLat, userLong, item.Latitude, item.Longitude).ToString() + " mi";
            }
        }
    }
}

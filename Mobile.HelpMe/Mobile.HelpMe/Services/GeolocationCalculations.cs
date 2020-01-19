using System;
using Mobile.HelpMe.Interfaces.Services;
using PrePass.Common.Gis;
using PrePass.Common.Gis.Calculations;

namespace Mobile.HelpMe.Services
{
    public class GeolocationCalculations : IGeolocationCalculations
    {
        public double CalculateDistance(double userLat, double userLon, double destinationLat, double destinationLon)
        {
            var userLocation = new GisPosition { Latitude = userLat, Longitude = userLon };
            var destLocation = new GisPosition { Latitude = destinationLat, Longitude = destinationLon };

            var distance = Geographic.GetDistance(userLocation, destLocation);

            return ConvertMetersToMiles(distance);
        }

        public double ConvertMetersToMiles(double distanceInMeters)
        {
            var distanceKm = distanceInMeters / 1000;
            var distanceMi = distanceKm / 1.609344;
            return Math.Round(distanceMi, 1);
        }

    }
}

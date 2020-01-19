using System;
namespace Mobile.HelpMe.Interfaces.Services
{
    public interface IGeolocationCalculations
    {
        double CalculateDistance(double userLat, double userLon, double destinationLat, double destinationLon);
        double ConvertMetersToMiles(double distanceInMeters);
    }
}

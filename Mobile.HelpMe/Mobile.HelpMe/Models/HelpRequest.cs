using System;
namespace Mobile.HelpMe.Models
{
    public class HelpRequest
    {
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public string Problem { get; set; }
        public string Description { get; set; }
        public string Username { get; set; }
        public string UserEmail { get; set; }
        public string Location
        {
            get => $"{Latitude}, {Longitude}";
        }
    }
}

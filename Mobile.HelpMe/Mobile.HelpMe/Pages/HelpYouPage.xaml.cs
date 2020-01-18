using System;
using System.Collections.Generic;
using Mobile.HelpMe.Models;
using Xamarin.Forms;

namespace Mobile.HelpMe.Pages
{
    public partial class HelpYouPage : ContentPage
    {
        public List<HelpRequest> requests { get; set; }

        public HelpYouPage()
        {
            InitializeComponent();
            InitData();
            list.ItemsSource = requests;
        }

        void InitData()
        {
            requests = new List<HelpRequest>
            {
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745

                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
                new HelpRequest
                {
                    Username = "jcanode",
                    Problem = ProblemEnum.FlatTire,
                    Latitude = 34.13234,
                    Longitude = -110.83745
                },
            };
        }
    }
}

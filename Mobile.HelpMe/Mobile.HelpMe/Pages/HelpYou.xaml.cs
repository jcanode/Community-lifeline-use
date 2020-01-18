using System;
using System.Collections.Generic;
using Mobile.HelpMe.Models;
using Xamarin.Forms;

namespace Mobile.HelpMe.Pages
{
    
    public partial class HelpYou : ContentPage
    {
        public List<HelpRequest> requests { get; set; }

        public HelpYou()
        {
            InitData();
            list.ItemsSource = rew
            InitializeComponent();
        }

        void InitData()
        {
            requests = new List<HelpRequest>
            {
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                },
                new HelpRequest
                {
                    Problem = ProblemEnum.FlatTire,
                    Username = "jcanode"
                }

            };
        }
    }
}

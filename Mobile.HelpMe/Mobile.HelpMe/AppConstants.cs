using System;
using System.Collections.Generic;

namespace Mobile.HelpMe
{
    public class AppConstants
    {
        public static IList<string> Categories { get; } = new List<string>
        {
            "Car",
            "Natural Disaster",
            "Other"
        };

        public static IList<string> CarProblems { get; } = new List<string>
        {
            "Flat Tire",
            "Stuck",
            "Need Tow",
            "Jump Battery",
            "Out Of Gas"
        };

        public static IList<string> NaturalDisasterProblems { get; } = new List<string>
        {
            "Stranded",
            "Need Medical Supplies",
            "Need Water",
            "Need Food"
        };
    }
}

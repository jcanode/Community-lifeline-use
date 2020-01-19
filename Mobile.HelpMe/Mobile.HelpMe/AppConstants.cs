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
            "Out Of Gas",
            "Other"
        };

        public static IList<string> NaturalDisasterProblems { get; } = new List<string>
        {
            "Stranded",
            "Need Medical Supplies",
            "Need Water",
            "Need Food",
            "Other"
        };

        public const string RequestSentTitle = "Request Sent";
        public const string RequestSentMessage = "Your request has been sent out. ";
        public const string OkayText = "Okay";

        // Errors
        public const string PasswordsDontMatch = "The passwords you entered do not match";
        public const string PasswordLength = "The password you entered is to short.";
        public const string EmptyFieldError = "Cannot have empty fields.  Please fill in all the information.";

        // URLs
        public const string BaseUrl = "";


        // Validations Constants
        public const int PasswordLengthConstant = 6;
    }
}

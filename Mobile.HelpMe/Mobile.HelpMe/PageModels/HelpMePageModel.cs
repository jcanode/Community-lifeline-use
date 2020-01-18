using System;
using System.Collections.Generic;
using FreshMvvm;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.PageModels
{
    public class HelpMePageModel : FreshBasePageModel
    {
        #region Picker Lists
        public IList<string> Categories { get; } = AppConstants.Categories;
        public IList<string> ProblemList { get; }

        public HelpMePageModel()
        {

        }
    }
}

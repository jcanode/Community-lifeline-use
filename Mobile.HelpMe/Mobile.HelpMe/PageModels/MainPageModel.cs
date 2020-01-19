using System;
using System.Threading.Tasks;
using System.Windows.Input;
using FreshMvvm;
using Xamarin.Forms;

namespace Mobile.HelpMe.PageModels
{
    public class MainPageModel : FreshBasePageModel
    {

        #region Commands
        public ICommand NeedHelpClicked { get; }
        public ICommand HelpSomeoneClicked { get; }
        #endregion

        public MainPageModel()
        {
            NeedHelpClicked = new Command(async () => await OnNeedHelpClicked());
            HelpSomeoneClicked = new Command(async () => await OnHelpSomeoneClicked());
        }


        private async Task OnNeedHelpClicked()
        {
            await CoreMethods.SwitchSelectedTab<HelpMePageModel>();
        }

        private async Task OnHelpSomeoneClicked()
        {
            await CoreMethods.SwitchSelectedTab<HelpYouPageModel>();
        }
    }
}

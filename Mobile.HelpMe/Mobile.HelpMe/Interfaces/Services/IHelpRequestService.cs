using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.Interfaces.Services
{
    public interface IHelpRequestService
    {
        Task CreateNewHelpRequest(HelpRequest request);
        Task ResolveHelpRequest(HelpRequest request);
    }
}

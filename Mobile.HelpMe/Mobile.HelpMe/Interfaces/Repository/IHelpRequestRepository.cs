using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.Interfaces.Repository
{
    public interface IHelpRequestRepository
    {
        Task CreateHelpRequest(HelpRequest request);
        Task<HelpRequest> GetCurrentRequest(string username);
        Task ResolveHelpRequest(HelpRequest request);
    }
}

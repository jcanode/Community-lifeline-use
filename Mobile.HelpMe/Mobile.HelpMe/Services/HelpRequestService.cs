using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Interfaces.Repository;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.Models;
using Newtonsoft.Json;

namespace Mobile.HelpMe.Services
{
    public class HelpRequestService : IHelpRequestService
    {
        IHelpRequestRepository _helpReqRepo;

        public HelpRequestService(IHelpRequestRepository repo)
        {
            _helpReqRepo = repo;
        }

        public async Task CreateNewHelpRequest(HelpRequest request)
        {
            var jsonReqest = JsonConvert.SerializeObject(request);
            await _helpReqRepo.CreateHelpRequest(jsonReqest);

        }

        public async Task ResolveHelpRequest(HelpRequest request)
        {
            var resolveReq = JsonConvert.SerializeObject(request);
            await _helpReqRepo.ResolveHelpRequest(resolveReq);
        }
    }
}

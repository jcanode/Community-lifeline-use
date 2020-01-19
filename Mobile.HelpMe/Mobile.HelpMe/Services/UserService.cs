using System;
using System.Diagnostics;
using System.Threading.Tasks;
using Mobile.HelpMe.Interfaces.Repository;
using Mobile.HelpMe.Interfaces.Services;
using Mobile.HelpMe.Models;
using Newtonsoft.Json;

namespace Mobile.HelpMe.Services
{
    public class UserService : IUserService
    {
        IUserRepository _userRepository;

        public UserService(IUserRepository userRepo)
        {
            _userRepository = userRepo;
        }

        public async Task<double> CalculateHelpRating(User user)
        {
            throw new NotImplementedException();
        }

        public async Task CreateUser(User user)
        {
            throw new NotImplementedException();
        }

        public async Task SignIn(string username, string password)
        {
            var loginReq = new LoginRequest
            {
                Username = username,
                Password = password
            };
            var jsonData = JsonConvert.SerializeObject(loginReq);
            await _userRepository.Login(jsonData);
        }
    }
}

using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Interfaces.Repository;
using Mobile.HelpMe.Models;
using Newtonsoft.Json;

namespace Mobile.HelpMe.Repositories
{
    public class UserRepository : BaseRepository, IUserRepository
    {
        protected override string BaseUrl => _baseUrl;
        private string _baseUrl;


        public UserRepository()
        {
            _baseUrl = AppConstants.BaseUrl;
        }

        public async Task CreateUser(string jsonContent)
        {

        }

        public async  Task<User> FindUser(string username)
        {
            throw new NotImplementedException();
        }

        public async Task<User> Login(string jsonContent)
        {
            string path = "/user/authenticate";
            var resp = await PostAsync(_baseUrl, path, jsonContent);
            var user = JsonConvert.DeserializeObject<User>(resp.Content.ToString());
            return user;
        }

        public async Task UpdateUser(User user)
        {
            throw new NotImplementedException();
        }
    }
}

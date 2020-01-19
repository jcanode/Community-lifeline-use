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
            _baseUrl = "http://hackaz.justincanode.com/api/users";
        }

        public async Task CreateUser(string jsonContent)
        {
            var path = "/users";
            var resp = await PostAsync(_baseUrl, path, jsonContent);
        }

        public async Task<User> FindUser(string username)
        {
            string path = "/user/username";
            var resp = await Get(_baseUrl, path);
            var user = JsonConvert.DeserializeObject<User>(resp.Content.ToString());
            return user;
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

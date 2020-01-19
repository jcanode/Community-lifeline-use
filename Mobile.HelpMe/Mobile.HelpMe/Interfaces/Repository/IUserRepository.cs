using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.Interfaces.Repository
{
    public interface IUserRepository
    {
        Task CreateUser(string jsonData);
        Task<User> FindUser(string username);
        Task<User> Login(string jsonData);
        Task UpdateUser(User user);
    }
}

using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.Interfaces.Repository
{
    public interface IUserRepository
    {
        Task CreateUser(string username, string password, string email);
        Task<User> FindUser(string username);
        Task<User> Login(string username, string password);
        Task UpdateUser(User user);
    }
}

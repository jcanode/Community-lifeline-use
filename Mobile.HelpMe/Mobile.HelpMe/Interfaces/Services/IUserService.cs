using System;
using System.Threading.Tasks;
using Mobile.HelpMe.Models;

namespace Mobile.HelpMe.Interfaces.Services
{
    public interface IUserService
    {
        Task<double> CalculateHelpRating(User user);
        Task SignIn(string username, string password);
        Task CreateUser(User user);
    }
}

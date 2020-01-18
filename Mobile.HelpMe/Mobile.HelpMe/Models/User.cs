using System;
namespace Mobile.HelpMe.Models
{
    public class User
    {
        public string UserName { get; set; }
        public string Password { get; set; }
        public string Email { get; set; }
        public int HelpRating { get; set; }
    }
}

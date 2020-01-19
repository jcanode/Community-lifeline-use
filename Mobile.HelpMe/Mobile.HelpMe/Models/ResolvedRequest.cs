using System;
namespace Mobile.HelpMe.Models
{
    public class ResolvedRequest
    {
        public int Id { get; set; }
        public string VictimUsername { get; set; }
        public string HelperUsername { get; set; }
        public string VictimEmail { get; set; }
    }
}

using System;
using System.Diagnostics;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Mobile.HelpMe.Repositories
{
    public class BaseRepository
    {
        protected HttpClient _client = new HttpClient();
        protected virtual string BaseUrl { get; }
        protected virtual TimeSpan Timeout
        {
            get => TimeSpan.FromMinutes(1);
        }

        public BaseRepository()
        {
        }

        protected async Task<HttpResponseMessage> Get(string url, string path)
        {
            var uri = $"{url}/{path}";

            using(var client = new HttpClient())
            {
                var resp = await client.GetAsync(uri);
                if (resp.StatusCode != System.Net.HttpStatusCode.OK)
                    Debug.WriteLine("Error retreiving data from API. " + resp.StatusCode);
                return resp;
            }
            
        }

        protected async Task<HttpResponseMessage> PostAsync(string url, string path, string body)
        {
            var uri = $"{url}/{path}";

            using (var client = new HttpClient())
            {
                var resp = await client.PostAsync(uri, new StringContent(body));
                if (resp.StatusCode != System.Net.HttpStatusCode.OK)
                    Debug.WriteLine($"Error posting to api. {resp.StatusCode}");
                return resp;
            }
        }
    }
}

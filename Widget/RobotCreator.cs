using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using System.Reflection.Metadata.Ecma335;

namespace Widget
{
    public class RobotCreator
    {
        public Robot CreateRobot()
        {
            IHost host = Host.CreateDefaultBuilder()
                .ConfigureServices((_, services) =>
                {
                    services
                        .AddSingleton<Robot>();
                })
                .Build();
            Robot robot = host.Services.GetRequiredService<Robot>();
            return robot;
        }
    }
}

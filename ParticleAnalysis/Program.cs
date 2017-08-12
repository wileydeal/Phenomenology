using System;
using System.IO;
using System.Diagnostics;

namespace ParticleAnalysis
{
	public class Program
	{
		public Program()
		{
		}
		public static void Main(string[] args)
		{
			ProcessStartInfo startInfo = new ProcessStartInfo();
			startInfo.Arguments = args.ToString();
			startInfo.FileName = "/Users/BlackMetal/root-6.06.04/bin/root.exe";
			Process launchroot = new Process();
			launchroot.StartInfo = startInfo;
			launchroot.Start();
		}
	}
}


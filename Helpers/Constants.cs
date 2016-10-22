using System;

namespace Helpers
{
    /*
        ## Android Application Name ##

        1. Droid/MainActivity.cs
            -   Add: Label = Constants.Product
        2. Droid/Properties/AndroidManifest.xml
            -   Remove: application:android:label="Project.Droid"
        3. Droid/Properties/AssemblyInfo.cs
            -   Add: using Project;
            -   Add: [assembly: Application(Label=Constants.Product)]

        ## iOS Application Name ##

        1. Just edit the Info.plist and set the Application Name

        ## Version ##

            1.  Add the follow Before Build custom command in all projects
                -   Command: python Script/pre-build.py
                -   Working: ${ProjectDir}
            2.  Increment version number in Solution Options -> Main Settings

        # Package #

        In all project set "org.company.project" to the Project Description

        TODO use this information
    */

    public static class Constants
    {
        public static string CurrentCopyright {
            get {
                var current = Math.Max(StartCopyright, DateTime.Now.Year);
                if (current == StartCopyright) {
                    return Copyright;
                } else {
                    return Copyright + "-" + current;
                }
            }
        }

        /* public static string LocalizedVersion {
            get {
                return String.Format("Versão {0}", VersionName);
            }
        } */

        public const string Company = "N42 Software";
        public const string Product = "Xamarin.Helpers";
        public const string Description = Product;
        public const int StartCopyright = 2016;
        public const string Copyright = "Copyright © N42 Software 2016";
        public const string Trademark = "";

        public const string VersionName = Version.Name;
        public const string FileVersion = Version.Name;
        public const string Package = Version.Package;

        /* public static string HockeyAppIdAndroid = "55126a6f69584506bb6123736662339c";
        public static string HockeyAppIdiOS = "b44f715683ff4fc89691db096ace790d";
        public static bool HockeyAppEnabled = true;
        public static bool HockeyAppMetricsEnabled = true;
        public static bool HockeyAppUpdateEnabled = false; */

        // public static string DatabaseName = "helpers.db3";

#if DEBUG
        /* public static SignUp DefaultSignUp = new SignUp {
            Name = "Debug User",
            Email = "debug@helpers",
            Phone = "+555198765432",
            Password = "debug"
        }; */
        public static bool Development = true;
#else
        public static bool Development = false;
#endif
    }
}

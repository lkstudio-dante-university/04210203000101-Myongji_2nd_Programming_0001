using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 전역 상수 */
	public static partial class KE01Define {
		#region 기본
		// 해상도 {
		public const float G_DESIGN_SCREEN_WIDTH = 1920.0f;
		public const float G_DESIGN_SCREEN_HEIGHT = 1080.0f;

		public static readonly Vector3 G_DESIGN_SCREEN_SIZE = new Vector3(KE01Define.G_DESIGN_SCREEN_WIDTH, KE01Define.G_DESIGN_SCREEN_HEIGHT, 0.0f);
		// 해상도 }

		// 카메라
		public const float G_DISTANCE_CAMERA_FAR_PLANE = 25000.0f;
		public const float G_DISTANCE_CAMERA_NEAR_PLANE = 0.1f;

		// 물리
		public static readonly Vector3 G_PHYSICS_GRAVITY = new Vector3(0.0f, -1960.0f, 0.0f);

		// 씬 이름
		public const string G_SCENE_N_EXAMPLE_00 = "E01Example_00 (Etc)";
		public const string G_SCENE_N_EXAMPLE_01 = "E01Example_01 (Basic)";
		public const string G_SCENE_N_EXAMPLE_02 = "E01Example_02 (Camera)";
		public const string G_SCENE_N_EXAMPLE_03 = "E01Example_03 (Prefab, Script)";
		public const string G_SCENE_N_EXAMPLE_04 = "E01Example_04 (Light, Material)";
		public const string G_SCENE_N_EXAMPLE_05 = "E01Example_05 (C# Basic - Data Type, Variable)";
		public const string G_SCENE_N_EXAMPLE_06 = "E01Example_06 (C# Basic - Collection)";
		public const string G_SCENE_N_EXAMPLE_07 = "E01Example_07 (C# Basic - Class)";
		public const string G_SCENE_N_EXAMPLE_08 = "E01Example_08 (C# Basic - Inheritance, Polymorphism)";
		public const string G_SCENE_N_EXAMPLE_09 = "E01Example_09 (C# Basic - Virtual Method)";
		public const string G_SCENE_N_EXAMPLE_10 = "E01Example_10 (C# Basic - User Define Data Type)";
		public const string G_SCENE_N_EXAMPLE_11 = "E01Example_11 (Physics)";
		public const string G_SCENE_N_EXAMPLE_12 = "E01Example_12 (Flappy Bird - Title)";
		public const string G_SCENE_N_EXAMPLE_13 = "E01Example_13 (Flappy Bird - Play)";
		public const string G_SCENE_N_EXAMPLE_14 = "E01Example_14 (Flappy Bird - Result)";
		public const string G_SCENE_N_EXAMPLE_15 = "E01Example_15 (Sprite, Animation)";
		public const string G_SCENE_N_EXAMPLE_16 = "E01Example_16 (GUI)";
		public const string G_SCENE_N_EXAMPLE_17 = "E01Example_17 (Moly Moly - Start)";
		public const string G_SCENE_N_EXAMPLE_18 = "E01Example_18 (Moly Moly - Play)";
		public const string G_SCENE_N_EXAMPLE_19 = "E01Example_19 (Moly Moly - Result)";
		public const string G_SCENE_N_EXAMPLE_20 = "E01Example_20 (Navigation Mesh)";
		public const string G_SCENE_N_EXAMPLE_21 = "E01Example_21 (Shader)";
		#endregion // 기본
	}
}

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

		// 씬 이름
		public const string G_SCENE_N_EXAMPLE_00 = "E01Example_00 (메뉴)";
		public const string G_SCENE_N_EXAMPLE_01 = "E01Example_01 (기초)";
		public const string G_SCENE_N_EXAMPLE_02 = "E01Example_02 (카메라)";
		public const string G_SCENE_N_EXAMPLE_03 = "E01Example_03 (프리팹 및 스크립트)";
		public const string G_SCENE_N_EXAMPLE_04 = "E01Example_04 (광원 및 재질)";
		public const string G_SCENE_N_EXAMPLE_05 = "E01Example_05 (C# 기초 - 자료형 및 변수)";
		public const string G_SCENE_N_EXAMPLE_06 = "E01Example_06 (C# 기초 - 컬렉션)";
		public const string G_SCENE_N_EXAMPLE_07 = "E01Example_07 (C# 기초 - 클래스)";
		public const string G_SCENE_N_EXAMPLE_08 = "E01Example_08 (C# 기초 - 상속 및 다형성)";
		public const string G_SCENE_N_EXAMPLE_09 = "E01Example_09 (C# 기초 - 가상 메서드)";
		public const string G_SCENE_N_EXAMPLE_10 = "E01Example_10 (C# 기초 - 사용자 정의 자료형)";
		public const string G_SCENE_N_EXAMPLE_11 = "E01Example_11 (물리)";
		public const string G_SCENE_N_EXAMPLE_12 = "E01Example_12 (플래피 버드 - 시작)";
		public const string G_SCENE_N_EXAMPLE_13 = "E01Example_13 (플래피 버드 - 플레이)";
		public const string G_SCENE_N_EXAMPLE_14 = "E01Example_14 (플래피 버드 - 결과)";
		#endregion // 기본
	}
}

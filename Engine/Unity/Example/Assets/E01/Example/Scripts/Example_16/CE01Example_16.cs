#define E16_IMGUI
#define E16_UNITY_GUI

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace E01 {
	/** Example 16 */
	public partial class CE01Example_16 : CE01SceneManager {
		#region 변수
		[Header("=====> UIs <=====")]
		[SerializeField] private Button m_oUnityGUIBtn = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_16;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}

		/** GUI 를 그린다 */
		public virtual void OnGUI() {
#if E16_IMGUI
			var stRect = new Rect(0.0f, 0.0f, Camera.main.pixelWidth, 50.0f);

			// 버튼을 눌렀을 경우
			if(GUI.Button(stRect, "버튼")) {
				Debug.Log("버튼을 눌렀습니다.");
			}
#endif // #if E16_IMGUI
		}
		#endregion // 함수
	}
}

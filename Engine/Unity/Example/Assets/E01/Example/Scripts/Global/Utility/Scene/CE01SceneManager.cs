using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 씬 관리자 */
	public abstract partial class CE01SceneManager : CE01Component {
		#region 프로퍼티
		public abstract string SceneName { get; }
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

			Physics.gravity = KE01Define.G_PHYSICS_GRAVITY;
			Application.targetFrameRate = Mathf.RoundToInt((float)Screen.currentResolution.refreshRateRatio.value);
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

			// 뒤로가기 키를 눌렀을 경우
			if(Input.GetKeyDown(KeyCode.Escape) && !this.SceneName.Equals(KE01Define.G_SCENE_N_EXAMPLE_00)) {
				CE01SceneLoader.Inst.LoadScene(KE01Define.G_SCENE_N_EXAMPLE_00);
			}
		}
		#endregion // 함수
	}
}

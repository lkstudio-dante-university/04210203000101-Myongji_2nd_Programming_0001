using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace E01 {
	/** Example 19 */
	public partial class CE01Example_19 : CE01SceneManager {
		#region 변수
		[Header("=====> UIs <=====")]
		[SerializeField] private Text m_oResultText = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_19;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}

		/** 상태를 갱신한다 */
		public override void UpdateState() {
			base.UpdateState();
			this.UpdateUIsState();
		}

		/** 다시하기 버튼을 눌렀을 경우 */
		public void OnTouchRetryBtn() {
			CE01SceneLoader.Inst.LoadScene(KE01Define.G_SCENE_N_EXAMPLE_18);
		}

		/** 그만두기 버튼을 눌렀을 경우 */
		public void OnTouchLeaveBtn() {
			CE01SceneLoader.Inst.LoadScene(KE01Define.G_SCENE_N_EXAMPLE_17);
		}

		/** UI 상태를 갱신한다 */
		private void UpdateUIsState() {
			m_oResultText.text = string.Format("점수 : {0}", CE01DataStorage_18.Inst.Score);
		}
		#endregion // 함수
	}
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** Example 21 */
	public partial class CE01Example_21 : CE01SceneManager {
		#region 변수
		private float m_fCutout = 0.0f;

		[SerializeField] private GameObject m_oTarget01 = null;
		[SerializeField] private GameObject m_oTarget02 = null;
		[SerializeField] private GameObject m_oTargetRoot = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_21;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

			for(int i = 0; i < m_oTargetRoot.transform.childCount; ++i) {
				var oTarget = m_oTargetRoot.transform.GetChild(i);
				oTarget.Rotate(Vector3.up * 90.0f * Time.deltaTime, Space.World);
			}

			// 상/하 방향 키를 눌렀을 경우
			if(Input.GetKey(KeyCode.UpArrow) || Input.GetKey(KeyCode.DownArrow)) {
				float fOffset = Input.GetKey(KeyCode.UpArrow) ? Time.deltaTime : -Time.deltaTime;
				m_fCutout = Mathf.Clamp01(m_fCutout + fOffset);

				var oMeshRenderer = m_oTarget02.GetComponent<MeshRenderer>();
				oMeshRenderer.material.SetFloat("_Cutout", m_fCutout);
			}
		}
		#endregion // 함수
	}
}

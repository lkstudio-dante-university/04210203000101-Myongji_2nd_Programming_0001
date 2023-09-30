using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 해상도 처리자 */
	public class CE01ResolutionHandler : CE01Component {
		#region 변수
		[SerializeField] private EProjection m_eProjection = EProjection._3D;
		[SerializeField] private Camera m_oCamera = null;
		#endregion // 변수

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
			m_oCamera = m_oCamera ?? Camera.main;
		}

		/** 초기화 */
		public override void Start() {
			base.Start();
			this.SetupResolution();
		}

		/** 해상도를 설정한다 */
		public void SetupResolution(bool a_bIsResetPos = false) {
			m_oCamera.orthographic = m_eProjection == EProjection._2D;
			m_oCamera.orthographicSize = KE01Define.G_DESIGN_SCREEN_HEIGHT / 2.0f;
		}
		#endregion // 함수
	}
}

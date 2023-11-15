using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using DG.Tweening;

namespace E01 {
	/** Example 20 */
	public partial class CE01Example_20 : CE01SceneManager {
		#region 변수
		private Tween m_oMoveAni = null;

		[Header("=====> Game Objects <=====")]
		[SerializeField] private GameObject m_oTarget = null;
		[SerializeField] private GameObject m_oDynamicObstacle = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_20;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
			m_oMoveAni = m_oDynamicObstacle.transform.DOMoveX(300.0f, 2.0f).SetAutoKill().SetEase(Ease.Linear).SetLoops(-1, LoopType.Yoyo);
		}

		/** 제거 되었을 경우 */
		public override void OnDestroy() {
			base.OnDestroy();
			m_oMoveAni?.Kill();
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

			// 마우스 버튼을 눌렀을 경우
			if(Input.GetMouseButtonDown((int)EMouseBtn.LEFT)) {
				this.HandleOnMouseBtnDown();
			}
		}

		/** 마우스 버튼 눌림을 처리한다 */
		private void HandleOnMouseBtnDown() {
			var stRay = this.MainCamera.ScreenPointToRay(Input.mousePosition);

			// 터치 된 물체가 존재 할 경우
			if(Physics.Raycast(stRay, out RaycastHit stRaycastHit)) {
				var oNavMeshAgent = m_oTarget.GetComponent<NavMeshAgent>();
				oNavMeshAgent.SetDestination(stRaycastHit.point);
			}
		}

#if UNITY_EDITOR
		/** 기즈모를 그린다 */
		public void OnDrawGizmos() {
			var stPrevColor = Gizmos.color;

			try {
				var stEndPos = m_oTarget.transform.position;
				stEndPos += m_oTarget.transform.forward * 250.0f;

				Gizmos.color = Color.red;
				Gizmos.DrawLine(m_oTarget.transform.position, stEndPos);
			} finally {
				Gizmos.color = stPrevColor;
			}
		}
#endif // #if UNITY_EDITOR
		#endregion // 함수
	}
}

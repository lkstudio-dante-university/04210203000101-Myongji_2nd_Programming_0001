using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * Note:
 * - 이벤트 함수 설명
 * - 장애물 스크립트 보완
 */
namespace E01 {
	/** 장애물 */
	public partial class CE01Obstacle_13 : CE01Component {
		#region 변수
		[SerializeField] private GameObject m_oSafeArea = null;
		[SerializeField] private GameObject m_oUpObstacle = null;
		[SerializeField] private GameObject m_oDownObstacle = null;
		#endregion // 변수

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}
		#endregion // 함수
	}
}

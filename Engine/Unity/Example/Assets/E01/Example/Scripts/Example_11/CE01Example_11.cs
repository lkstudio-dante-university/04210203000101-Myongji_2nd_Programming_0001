#define E11_PHYSICS_01
#define E11_PHYSICS_02

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** Example 11 */
	public partial class CE01Example_11 : CE01SceneManager {
		#region 변수
		[SerializeField] private GameObject m_oPhysics01Target = null;
		[SerializeField] private GameObject m_oPhysics02Target = null;

		[Header("=====> Root Game Objects <=====")]
		[SerializeField] private List<GameObject> m_oPhysics01RootList = new List<GameObject>();
		[SerializeField] private List<GameObject> m_oPhysics02RootList = new List<GameObject>();
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_11;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

#if E11_PHYSICS_01
			bool bIsActivePhysics01 = true;
#else
			bool bIsActivePhysics01 = false;
#endif // #if E11_PHYSICS_01

#if E11_PHYSICS_02
			bool bIsActivePhysics02 = true;
#else
			bool bIsActivePhysics02 = false;
#endif // #if E11_PHYSICS_02

			for(int i = 0; i < m_oPhysics01RootList.Count; ++i) {
				m_oPhysics01RootList[i].SetActive(bIsActivePhysics01);
			}

			for(int i = 0; i < m_oPhysics02RootList.Count; ++i) {
				m_oPhysics02RootList[i].SetActive(bIsActivePhysics02);
			}
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

#if E11_PHYSICS_01
			float fVertical = Input.GetAxis("Vertical");
			float fHorizontal = Input.GetAxis("Horizontal");

			m_oPhysics01Target.transform.Rotate(Vector3.up, fHorizontal * Time.deltaTime, Space.World);
			m_oPhysics01Target.transform.Translate(Vector3.forward * fVertical * Time.deltaTime, Space.Self);
#elif E11_PHYSICS_02

#endif // E11_PHYSICS_01
		}

#if UNITY_EDITOR
		/** 기즈모를 그린다 */
		public void OnDrawGizmos() {

		}
#endif // #if UNITY_EDITOR
#endregion // 함수
	}
}

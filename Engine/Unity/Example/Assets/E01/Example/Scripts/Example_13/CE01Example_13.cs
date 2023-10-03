using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace E01 {
	/** Example 13 */
	public partial class CE01Example_13 : CE01SceneManager {
		/** 상태 */
		private enum EState {
			NONE = -1,
			PLAY,
			GAME_OVER,
			[HideInInspector] MAX_VAL
		}

		#region 변수
		private EState m_eState = EState.PLAY;

		[Header("=====> UIs <=====")]
		[SerializeField] private Text m_oScoreText = null;

		[Header("=====> Game Objects <=====")]
		[SerializeField] private GameObject m_oTarget = null;
		[SerializeField] private GameObject m_oObstacleRoot = null;
		[SerializeField] private GameObject m_oOriginObstacle = null;

		private List<GameObject> m_oObstacleList = new List<GameObject>();
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_13;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
		}

		/** 초기화 */
		public override void Start() {
			base.Start();
			StartCoroutine(this.TryCreateObstacles());
		}

		/** 상태를 갱신한다 */
		public override void Update() {
			base.Update();

			// 플레이 상태가 아닐 경우
			if(m_eState != EState.PLAY) {
				return;
			}

			// 점프 키를 눌렀을 경우
			if(Input.GetKeyDown(KeyCode.Space)) {
				var oRigidbody = m_oTarget.GetComponent<Rigidbody>();
				oRigidbody.velocity = Vector3.zero;

				oRigidbody.AddForce(Vector3.up * 1000.0f, ForceMode.VelocityChange);
			}

			for(int i = 0; i < m_oObstacleList.Count; ++i) {
				m_oObstacleList[i].transform.localPosition += new Vector3(-550.0f * Time.deltaTime, 0.0f, 0.0f);
			}
		}
		#endregion // 함수
	}

	/** Example 13 - 코루틴 */
	public partial class CE01Example_13 : CE01SceneManager {
		#region 함수
		/** 장애물 생성을 시도한다 */
		private IEnumerator TryCreateObstacles() {
			do {
				var oObstacle = Instantiate(m_oOriginObstacle, Vector3.zero, Quaternion.identity);
				oObstacle.transform.SetParent(m_oObstacleRoot.transform, false);

				oObstacle.transform.localPosition = new Vector3((KE01Define.G_DESIGN_SCREEN_WIDTH / 2.0f) + 150.0f, 0.0f, 0.0f);

				m_oObstacleList.Add(oObstacle);
				yield return new WaitForSeconds(1.5f);
			} while(m_eState != EState.GAME_OVER);
		}
		#endregion // 함수
	}
}

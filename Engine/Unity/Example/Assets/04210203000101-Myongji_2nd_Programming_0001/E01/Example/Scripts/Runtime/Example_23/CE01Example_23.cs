using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.AI;
using TMPro;

namespace Example
{
	/** Example 23 */
	public class CE01Example_23 : CSceneManager
	{
		/** 상태 */
		public enum EState
		{
			NONE = -1,
			PLAY,
			GAME_OVER,
			[HideInInspector] MAX_VAL
		}

		#region 변수
		[SerializeField] private CE01Player_23 m_oPlayer = null;
		private bool m_bIsDirtyUpdateUIsState = true;

		private int m_nScore = 0;
		private EState m_eState = EState.PLAY;

		[Header("=====> UIs <=====")]
		[SerializeField] private TMP_Text m_oScoreText = null;

		[Header("=====> Game Objects <=====")]
		[SerializeField] private GameObject m_oBulletRoot = null;
		[SerializeField] private GameObject m_oOriginBullet = null;

		[SerializeField] private GameObject m_oMonsterRoot = null;
		[SerializeField] private GameObject m_oOriginMonster = null;

		[SerializeField] private List<GameObject> m_oMonsterSpawnPosList = new List<GameObject>();
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KDefine.G_N_SCENE_EXAMPLE_23;
		public CE01Player_23 Player => m_oPlayer;

		public CE01ObjsPoolManager_23 ObjsPoolManager { get; private set; } = null;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake()
		{
			base.Awake();

			var oObjsPoolManager = new GameObject("ObjsPoolManager");
			oObjsPoolManager.transform.SetParent(this.gameObject.transform, false);

			this.ObjsPoolManager = oObjsPoolManager.AddComponent<CE01ObjsPoolManager_23>();
		}

		/** 초기화 */
		public override void Start()
		{
			base.Start();
			StartCoroutine(this.TryCreateMonsters());
		}

		/** 상태를 갱신한다 */
		public override void Update()
		{
			base.Update();

			// 게임 종료 상태 일 경우
			if(this.IsGameOver())
			{
				return;
			}

			// UI 상태 갱신이 필요 할 경우
			if(m_bIsDirtyUpdateUIsState)
			{
				this.UpdateUIsState();
				m_bIsDirtyUpdateUIsState = false;
			}

			// 스페이스 키를 눌렀을 경우
			if(Input.GetKeyDown(KeyCode.Space))
			{
				m_oPlayer.Fire(m_oOriginBullet, m_oBulletRoot);
			}
		}

		/** 플레이어 사망 상태를 처리한다 */
		public void HandleOnDeathPlayer()
		{
			m_oPlayer.Update();

			m_eState = EState.GAME_OVER;
			CE01DataStorage_23.Inst.SetScore(m_nScore);

			CSceneLoader.Inst.LoadScene(KDefine.G_N_SCENE_EXAMPLE_24, false);
		}

		/** 몬스터 사망 상태를 처리한다 */
		public void HandleOnDeathMonster()
		{
			m_nScore += 10;
			m_bIsDirtyUpdateUIsState = true;
		}

		/** UI 상태를 갱신한다 */
		private void UpdateUIsState()
		{
			m_oScoreText.text = $"{m_nScore}";
		}

		/** 몬스터 생성을 시도한다 */
		private IEnumerator TryCreateMonsters()
		{
			do
			{
				var oMonster = (this.ObjsPoolManager.SpawnObj<CE01Monster_23>(() =>
				{
					var oGameObj = Instantiate(m_oOriginMonster, Vector3.zero, Quaternion.identity);
					oGameObj.transform.SetParent(m_oMonsterRoot.transform, false);

					return oGameObj;
				}) as GameObject).GetComponent<CE01Monster_23>();

				int nPosIdx = Random.Range(0, m_oMonsterSpawnPosList.Count);
				int nWalkable = NavMesh.GetAreaFromName("Walkable");

				var oSpawnPos = m_oMonsterSpawnPosList[nPosIdx];

				// 위치를 계산했을 경우
				if(NavMesh.SamplePosition(oSpawnPos.transform.position,
					out NavMeshHit stNavMeshHit, float.MaxValue, 1 << nWalkable))
				{
					oMonster.transform.position = stNavMeshHit.position;
				}

				oMonster.Init();
				oMonster.gameObject.SetActive(true);

				yield return new WaitForSeconds(5.0f);
			} while(!this.IsGameOver());
		}
		#endregion // 함수

		#region 접근 함수
		/** 게임 종료 여부를 검사한다 */
		public bool IsGameOver()
		{
			return m_eState == EState.GAME_OVER;
		}
		#endregion // 접근 함수
	}
}

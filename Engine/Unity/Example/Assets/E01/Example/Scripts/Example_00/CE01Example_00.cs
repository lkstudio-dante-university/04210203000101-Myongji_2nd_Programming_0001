using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

namespace E01 {
	/** 메뉴 씬 */
	public partial class CE01Example_00 : CE01SceneManager {
		#region 변수
		[Header("=====> Game Objects <=====")]
		[SerializeField] private GameObject m_oOriginText = null;
		[SerializeField] private GameObject m_oScrollViewContents = null;
		#endregion // 변수

		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_00;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

			for(int i = 1; i < SceneManager.sceneCountInBuildSettings; ++i) {
				string oScenePath = SceneUtility.GetScenePathByBuildIndex(i);

				var oText = Instantiate(m_oOriginText, Vector3.zero, Quaternion.identity);
				oText.transform.SetParent(m_oScrollViewContents.transform, false);

				oText.GetComponent<Text>().text = Path.GetFileNameWithoutExtension(oScenePath);
				oText.GetComponent<Button>().onClick.AddListener(() => this.OnTouchText(oScenePath));
			}
		}

		/** 초기화 */
		public override void Start() {
			base.Start();
			LayoutRebuilder.ForceRebuildLayoutImmediate(m_oScrollViewContents.transform as RectTransform);
		}

		/** 텍스트를 눌렀을 경우 */
		private void OnTouchText(string a_oScenePath) {
			CE01SceneLoader.Inst.LoadScene(a_oScenePath);
		}
		#endregion // 함수
	}
}

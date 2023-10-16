using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 타겟 */
	public partial class CE01Target_18 : CE01Component {
		/** 타겟 타입 */
		public enum ETargetType {
			NONE = -1,
			A,
			D,
			[HideInInspector] MAX_VAL
		}

		#region 변수
		private bool m_bIsOpen = false;
		private Animator m_oAnimator = null;

		[SerializeField] private RuntimeAnimatorController m_oAniController01 = null;
		[SerializeField] private RuntimeAnimatorController m_oAniController02 = null;
		#endregion // 변수

		#region 프로퍼티
		public ETargetType TargetType { get; private set; } = ETargetType.NONE;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();
			m_oAnimator = this.GetComponent<Animator>();
		}

		/** 초기화 */
		public override void Start() {
			base.Start();
			StartCoroutine(this.TryOpen());
		}

		/** 캐치 상태를 처리한다 */
		public bool TryCatch() {
			// 오픈 상태 일 경우
			if(m_bIsOpen) {
				m_bIsOpen = false;
				m_oAnimator.SetTrigger("Catch");

				return true;
			}

			return false;
		}

		/** 애니메이션이 종료 상태를 처리한다 */
		private void HandleOnAniStateExit(CE01AniEventDispatcher a_oSender, Animator a_oAnimator, AnimatorStateInfo a_stStateInfo, int a_nLayerIdx) {
			StartCoroutine(this.TryOpen());
		}

		/** 등장 상태를 처리한다 */
		private IEnumerator TryOpen() {
			yield return new WaitForSeconds(Random.Range(1.0f, 8.0f));
			this.SetTargetType((ETargetType)Random.Range(0, (int)ETargetType.MAX_VAL));

			m_bIsOpen = true;
			m_oAnimator.runtimeAnimatorController = (this.TargetType <= ETargetType.A) ? m_oAniController01 : m_oAniController02;

			m_oAnimator.SetTrigger("Open");
			m_oAnimator.ResetTrigger("Catch");

			var oAniEventDispatchers = m_oAnimator.GetBehaviours<CE01AniEventDispatcher>();

			for(int i = 0; i < oAniEventDispatchers.Length; ++i) {
				oAniEventDispatchers[i].SetAniStateExitCallback(this.HandleOnAniStateExit);
			}
		}
		#endregion // 함수

		#region 접근 함수
		/** 타겟 타입을 변경한다 */
		public void SetTargetType(ETargetType a_eType) {
			this.TargetType = a_eType;
		}
		#endregion // 접근 함수
	}
}

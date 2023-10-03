using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace E01 {
	/** 충돌 전달자 */
	public partial class CE01CollisionDispatcher : CE01Component {
		#region 프로퍼티
		public System.Action<CE01CollisionDispatcher, Collision> EnterCallback { get; private set; } = null;
		public System.Action<CE01CollisionDispatcher, Collision> StayCallback { get; private set; } = null;
		public System.Action<CE01CollisionDispatcher, Collision> ExitCallback { get; private set; } = null;

		public System.Action<CE01CollisionDispatcher, Collision2D> Enter2DCallback { get; private set; } = null;
		public System.Action<CE01CollisionDispatcher, Collision2D> Stay2DCallback { get; private set; } = null;
		public System.Action<CE01CollisionDispatcher, Collision2D> Exit2DCallback { get; private set; } = null;
		#endregion // 프로퍼티

		#region 함수
		/** 충돌이 시작 되었을 경우 */
		public void OnCollisionEnter(Collision a_oCollision) {
			this.EnterCallback?.Invoke(this, a_oCollision);
		}

		/** 충돌이 진행 중 일 경우 */
		public void OnCollisionStay(Collision a_oCollision) {
			this.StayCallback?.Invoke(this, a_oCollision);
		}

		/** 충돌이 종료 되었을 경우 */
		public void OnCollisionExit(Collision a_oCollision) {
			this.ExitCallback?.Invoke(this, a_oCollision);
		}

		/** 충돌이 시작 되었을 경우 */
		public void OnCollisionEnter2D(Collision2D a_oCollision) {
			this.Enter2DCallback?.Invoke(this, a_oCollision);
		}

		/** 충돌이 진행 중 일 경우 */
		public void OnCollisionStay2D(Collision2D a_oCollision) {
			this.Stay2DCallback?.Invoke(this, a_oCollision);
		}

		/** 충돌이 종료 되었을 경우 */
		public void OnCollisionExit2D(Collision2D a_oCollision) {
			this.Exit2DCallback?.Invoke(this, a_oCollision);
		}
		#endregion // 함수

		#region 접근 함수
		/** 시작 콜백을 변경한다 */
		public void SetEnterCallback(System.Action<CE01CollisionDispatcher, Collision> a_oCallback) {
			this.EnterCallback = a_oCallback;
		}

		/** 진행 콜백을 변경한다 */
		public void SetStayCallback(System.Action<CE01CollisionDispatcher, Collision> a_oCallback) {
			this.StayCallback = a_oCallback;
		}

		/** 종료 콜백을 변경한다 */
		public void SetExitCallback(System.Action<CE01CollisionDispatcher, Collision> a_oCallback) {
			this.ExitCallback = a_oCallback;
		}

		/** 시작 콜백을 변경한다 */
		public void SetEnter2DCallback(System.Action<CE01CollisionDispatcher, Collision2D> a_oCallback) {
			this.Enter2DCallback = a_oCallback;
		}

		/** 진행 콜백을 변경한다 */
		public void SetStay2DCallback(System.Action<CE01CollisionDispatcher, Collision2D> a_oCallback) {
			this.Stay2DCallback = a_oCallback;
		}

		/** 종료 콜백을 변경한다 */
		public void SetExit2DCallback(System.Action<CE01CollisionDispatcher, Collision2D> a_oCallback) {
			this.Exit2DCallback = a_oCallback;
		}
		#endregion // 접근 함수
	}
}

import { useState, useRef } from 'react'

function VoiceRecorder({ onTranscription }) {
  const [isRecording, setIsRecording] = useState(false)
  const [isTranscribing, setIsTranscribing] = useState(false)
  const mediaRecorderRef = useRef(null)
  const chunksRef = useRef([])

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      const mediaRecorder = new MediaRecorder(stream)
      mediaRecorderRef.current = mediaRecorder
      chunksRef.current = []

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunksRef.current.push(e.data)
        }
      }

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(chunksRef.current, { type: 'audio/webm' })
        stream.getTracks().forEach(track => track.stop())
        await transcribeAudio(audioBlob)
      }

      mediaRecorder.start()
      setIsRecording(true)
    } catch (error) {
      console.error('Failed to start recording:', error)
      alert('Could not access microphone. Please check permissions.')
    }
  }

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop()
      setIsRecording(false)
    }
  }

  const transcribeAudio = async (audioBlob) => {
    setIsTranscribing(true)
    try {
      console.log('Audio blob size:', audioBlob.size, 'type:', audioBlob.type)

      const formData = new FormData()
      formData.append('file', audioBlob, 'recording.webm')

      const response = await fetch('/transcribe', {
        method: 'POST',
        body: formData
      })

      const data = await response.json()

      if (!response.ok) {
        console.error('Transcription API error:', data)
        throw new Error(data.detail || 'Transcription failed')
      }

      if (data.text) {
        onTranscription(data.text)
      }
    } catch (error) {
      console.error('Transcription error:', error)
      alert(`Transcription failed: ${error.message}`)
    } finally {
      setIsTranscribing(false)
    }
  }

  const handleClick = () => {
    if (isRecording) {
      stopRecording()
    } else {
      startRecording()
    }
  }

  return (
    <button
      type="button"
      className={`voice-button ${isRecording ? 'recording' : ''} ${isTranscribing ? 'transcribing' : ''}`}
      onClick={handleClick}
      disabled={isTranscribing}
      title={isRecording ? 'Stop recording' : 'Start voice recording'}
    >
      {isTranscribing ? (
        <span className="transcribing-icon">...</span>
      ) : (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
          <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
          <line x1="12" y1="19" x2="12" y2="23" />
          <line x1="8" y1="23" x2="16" y2="23" />
        </svg>
      )}
    </button>
  )
}

export default VoiceRecorder

import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://intelligent-content-moderation.onrender.com',
  headers: {
    'Content-Type': 'application/json',
  },
})

/**
 * Sends content to the moderation backend for analysis, risk
 * assessment, and a final decision.
 *
 * @param {string} content - The raw text submitted for review.
 * @returns {Promise<{analysis: object, risk: object, decision: object}>}
 */
export async function moderateContent(content) {
  const response = await apiClient.post('/moderate', { content })
  return response.data
}

export default apiClient

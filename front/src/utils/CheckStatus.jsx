import endpoints from './endpoints.jsx';
import { Fetcher } from './Fetch.jsx';

export async function CheckStatus() {
  try {
    const baseUrl = endpoints();
    const fullUrl = `${baseUrl}/api/v1/auth/status/`;
    
    console.log('Выполняем запрос к:', fullUrl);

    const response = await Fetcher(fullUrl);

    console.log('Статус ответа:', response.status);

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Ошибка:', errorText);
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    let jsonData;
    try {
      jsonData = await response.json();
      console.log('Разобрано JSON:', jsonData);
    } catch (error) {
      console.error('Не удалось разобрать JSON:', error);
      const textResponse = await response.text();
      console.log('Сырой текстовый ответ:', textResponse);
      if (textResponse.startsWith('<')) {
        console.error('Ответ содержит HTML!');
      } else {
        console.log('Неизвестный формат ответа:', textResponse);
      }
      throw new Error('Неправильный формат ответа');
    }

    return jsonData;
  } catch (error) {
    console.error('Пиздец:', error);
    throw error;
  }
}

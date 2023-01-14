//Alarm to study 
chrome.alarms.onAlarm.addListener(() => {
    chrome.action.setBadgeText({ text: '' });
    chrome.notifications.create({
      type: 'basic',
      iconUrl: 'icon.png',
      title: 'Study Guide',
      message: 'Time to Study!',
      buttons: [
        { title: 'Keep going' }
      ],
      priority: 0
    });
  });

  //Alarm is started
  chrome.notifications.onButtonClicked.addListener(async () => {
    const item = await chrome.storage.sync.get(['minutes']);
    chrome.action.setBadgeText({ text: 'ON' });
    chrome.alarms.create({ delayInMinutes: item.minutes });
  });

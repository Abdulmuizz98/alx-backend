export default function createPushNotificationsJobs(jobs, queue){
  if(!Array.isArray(jobs)) throw new Error('Job is not an array');
  for (let j of jobs){
    let job = queue.create('push_notification_code_3', j).save((err) => {
      if (!err) console.log('Notification job created:')
    })
    job.on('complete', (result) => {console.log('Notification job', job.id, 'completed')});
    job.on('failed', (err) => {console.log('Notification job', job.id, 'failed:', err)});
    job.on('progress', (progress, data) => {console.log(`Notification job ${job.id} ${progress}% complete`)});

  }
}

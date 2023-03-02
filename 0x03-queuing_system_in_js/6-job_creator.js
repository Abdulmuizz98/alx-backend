import kue from 'kue';

const queue = kue.createQueue();

const job_meta = {
  phoneNumber: '0800000',
  message: 'Thanks you just got a notification',
}

const job = queue.create('push_notification_code', job_meta).save((err) => {
 if (!err) console.log('Notification job created:', job.id)
})

job.on('complete', (result) => {console.log('Notification job completed')})
job.on('failed', (err) => {console.log('Notification job failed')})

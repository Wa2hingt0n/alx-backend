// Creates a queue with 'Kue'
import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const jobData = {
    phoneNumber: '0700123456',
    message: 'This is my message'
}

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
    console.log('Notification job created', job.id);
});

job.on('complete', () => {
    console.log('Notification job complete');
});

job.on('failed', (errorMessage) => {
    console.log('Notification job failed');
});

job.save();

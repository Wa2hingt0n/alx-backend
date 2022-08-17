// Creates a queue with 'Kue'
import { createQueue } from 'kue';

const push_notification_code = createQueue();

const jobData = {
    phoneNumber: '0700123456',
    message: 'This is my message'
}

const job = push_notification_code.create(
    'Notification', jobData).save((err) => {
	if (!err) {
	    console.log('Notification job created:', job.id);
	}
    });

job.on('complete', (result) => {
    console.log('Notification job complete');
});

job.on('failed', (errorMessage) => {
    console.log('Notification job failed');
});
